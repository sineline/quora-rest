<template>
    <main class="container-main">
		<h1 v-if="!question_data.id">Ask a Question</h1>
		<h1 v-else>Edit the Question</h1>
		<textarea rows="3" placeholder="What do you want to ask?" v-model="question_data.title"></textarea>
		<button class="btn-publish btn btn-success" v-on:click="publish()">Publish</button>
    </main>
</template>

<script>
	import QuestionLinkMixin from '@/mixins/QuestionLink.vue';
	import APIRequest from '@/common/api_request'

	export default {
		name: 'AskQuestion',
		mixins: [QuestionLinkMixin],
		data: function () {
			return {
				question_data : {
					id : null,
					title : "",
				}
			}
		},
		created() {
			if(this.question_prop){
				this.question_data = this.question_prop;
			}
		}, 
		props: {
			question_prop : Object
		},
		methods: {
			publish(){
				const post_data = { 
					title: this.question_data.title,
				}

				const endpoint = (typeof this.question_prop !== 'undefined')
					? "http://localhost:8000/api/questions/"+this.question_prop.id+"/" 
					: "http://localhost:8000/api/questions/";
				
				const method = this.question_prop ? 'PUT' : 'POST';
				new APIRequest(endpoint, method, post_data).call_api().then((data) => {
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
