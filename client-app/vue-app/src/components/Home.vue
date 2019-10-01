<template>
	<main>
		<header>
			<div class="container-main container-header">
				<h3 class="title-site">Question Time</h3>
				<div class="container-button">
					<router-link class="btn btn-success" to='/'>Home</router-link>
					<router-link class="btn btn-danger" to='/ask-question'>Ask a question</router-link>
					<button class="btn btn-light" v-on:click="logout()">Logout</button>
				</div>
			</div>
		</header>
		<div class="container-main">
			<ul>
				<Question 
					v-for="question in questions"
					v-bind:key="question.id"
					v-bind:question="question"/>
			</ul>
		</div>
	</main>
</template>

<script>
	import Question from './Question.vue'

	export default {
		components: {
			Question
		},
		name: 'Home',
		data: function () {
			return {
				questions : []
			}
		},
		mounted() {
			// If not token - we redirect to login
			if(!localStorage.token){
				this.$router.push({ name: 'login'});
				return;
			}

			fetch("http://localhost:8000/api/questions/", {
				method: 'GET',
				headers: {
					'Authorization': 'Token '+localStorage.token
				},
			})
			.then(response =>response.json())
			.then((data) => {
				//this.posts = data;
				//console.debug(response);
				console.debug(data);
				this.questions = data;
			});
		}, 
		props: {
		},
		methods: {
			logout() {
				localStorage.token = null;
				this.$router.push({ name: 'login'});
			}
		},
	}
</script>

<style>
	#app {
		margin-top: 0px;
	}
</style>
<style scoped>
	header{
		background: #f6f6f6;
		width: 100vw;
		padding: 10px;
	}
	.container-main{
		width: 80vw;
		margin:auto;
	}
	.container-main ul{
		padding:0;
		margin:0;
	}
	.container-header{
		display: inline-grid;
		grid-template-columns: auto auto; 
	}
	header .title-site{
		justify-self: start;
		align-self: center;
		font-family: serif;
	}
	header .container-button{
		justify-self: end;
	}
	header .container-button .btn{
		margin: 0 2px;
	}
	
</style>
