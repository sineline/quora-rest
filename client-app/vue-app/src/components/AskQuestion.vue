<template>
    <main class="container-main">
       <h1>Ask a Question</h1>
	   <textarea rows="3" placeholder="What do you want to ask?" v-model="question"></textarea>
	   <button class="btn-publish btn btn-success" v-on:click="publish()">Publish</button>
    </main>
</template>

<script>
	import QuestionLinkMixin from '../mixin/QuestionLink.vue';

	export default {
		name: 'AskQuestion',
		mixins: [QuestionLinkMixin],
		data: function () {
			return {
				question : ""
			}
		},
		mounted() {
			
		}, 
		props: {
		},
		methods: {
			publish(){
				const post_data = { 
					title: this.question,
				}

				fetch("http://localhost:8000/api/questions/", {
					method: 'POST',
					headers: {
						'Content-Type': 'application/json',
						'Authorization': 'Token '+localStorage.token
					},
					body: JSON.stringify(post_data)
				})
				.then(response => response.json())
				.then((data) => {
					console.debug(data);

					this.$router.push(this.createLinkQuestion(data));
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
