<template>
  	<header>
		<div class="container-header">
			<h3 class="title-site">Question Time</h3>
			<div class="container-button">
				<router-link class="btn btn-success" to='/'>Home</router-link>
				<router-link class="btn btn-danger" to='/ask-question'>Ask a question</router-link>
				<button class="btn btn-light" v-on:click="logout()">Logout</button>
			</div>
		</div>
	</header>
</template>

<script>
export default {
	name: 'Home',
	data: function () {
		return {
		}
	},
	mounted() {
		// If not token - we redirect to login
		if(!localStorage.token){
			this.$router.push({ name: 'login'});
			return;
		}

		// fetch("https://jsonplaceholder.typicode.com/users")
		// 	.then(response => response.json())
		// 	.then((data) => {
		// 		this.users = data;
		// 	})
			
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
	.container-header{
		display: inline-grid;
		grid-template-columns: auto auto; 
		width: 80vw;
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
