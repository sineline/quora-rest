<template>
	<main>
		<div class="container-main">
			<ul>
				<Question 
					v-for="question in questions"
					v-bind:key="question.id"
					v-bind:question="question"/>

				<button  v-if="next_page" class="btn-load_more btn btn-success" v-on:click="load_more()">Load More</button>
			</ul>
		</div>
	</main>
</template>

<script>
	import Question from '../components/Question';
	import APIRequest from '../common/api_request'

	export default {
		name: 'Home',
		components: {
			Question
		},
		data: function () {
			return {
				questions : [],
				next_page: "",
				count_question: 0,
				more_question: true
			}
		},
		mounted() {
			// If not token - we redirect to login
			if(!localStorage.token){
				this.$router.push({ name: 'login'});
				return;
			}

			if(!this.questions.length)
				this.call_api("http://localhost:8000/api/questions/");
		}, 
		props: {
		},
		methods: {
			call_api(url_api){
				new APIRequest(url_api).call_api().then((data) => {
					this.questions = !this.questions.length ? data.results : this.questions.concat(data.results);
					this.count_question = data.count;
					this.next_page = data.next;
				});
			},
			logout() {
				localStorage.token = null;
				this.$router.push({ name: 'login'});
			},
			load_more() {
				this.call_api(this.next_page);
        	}
		},
	}
</script>

<style scoped>
	.container-main ul{
		padding:0;
		margin:0;
		text-align: left;
	}
	.btn-load_more{
		margin: 15px;
	}
</style>
