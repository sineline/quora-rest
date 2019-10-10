<template>
    <main class="container-main">
	   <h1>Edit your Answer</h1>
	   <textarea rows="3" placeholder="What do you want to ask?" v-model="answer.answer"></textarea>
	   <button class="btn-publish btn btn-success" v-on:click="publish()">Publish your answer</button>
    </main>
</template>

<script>

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
				fetch(url_api, {
					method: 'PUT',
					headers: {
						'Content-Type': 'application/json',
						'Authorization': 'Token '+localStorage.token
					},
					body: JSON.stringify(post_data)
				})
				.then(response => response.json())
				.then((data) => {
					console.debug(data);
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
