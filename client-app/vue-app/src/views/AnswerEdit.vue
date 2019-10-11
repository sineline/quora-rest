<template>
	<main class="container-main">
		<h1>Edit your Answer</h1>
		<textarea rows="3" placeholder="What do you want to ask?" v-model="answer.answer"></textarea>
		<button class="btn-publish btn btn-success" v-on:click="publish()">Publish your answer</button>
	</main>
</template>

<script>
	import APIRequest from '@/common/api_request'
	export default {
		name: 'AnswerEdit',
		data: function () {
			return {
				
			}
		},
		created() {
			
		}, 
		props: {
			answer: Object
		},
		methods: {
			publish(){
				const post_data = { 
					answer: this.answer.answer,
					question: this.answer.question
				}

				const url_api = "http://localhost:8000/api/answers/"+this.answer.id+"/";
				new APIRequest(url_api, 'PUT', post_data).call_api().then(() => {
					this.$router.go(-1);
				});
			},
        },
	}
</script>

<style>
	
</style>
<style scoped>
	.container-main {
		text-align: left;
	}
	textarea{
		width: 100%;
		border-radius: 7px;
		border-color: #dcdcdc;
		padding: 15px;
	}
	::placeholder{
		color: #aaa;
	}
</style>
