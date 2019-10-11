<template>
    <div class="question container-main">
        <h2 class="title-question">{{ question_data.title }}</h2>
        <div v-if="is_author">
            <router-link class="btn btn-outline-success" :to="link_ask_question">Edit</router-link>
            <button class="btn btn-outline-danger" v-on:click="delete_question()">Delete</button>
        </div>
        <div class="alert alert-danger" role="alert" v-if="error_api">{{ error_api }}</div>
        <p class="author">Posted by <span>{{ question_data.author_name }}</span></p>
        <p class="created">{{ question_data.created_date }}</p>
        <div class="container-button-answer">
            <div v-if="!is_answered">
                <button class="btn btn-success" v-on:click="set_is_answering(true)" v-if="!is_answering">Answer the Question</button>
                <div class="container-answering" v-if="is_answering">
                    <p>Answer the Question</p>
                    <textarea rows="4" placeholder="Answer the Question" v-model="answer_textarea"></textarea>
                    <button class="btn btn-success" v-on:click="submit_answer()">Submit your answer</button>
                </div>
            </div>
            <p v-else class="text-success">You have written an answer!</p>
        </div>
        <Answer 
            v-for="answer in answer_data"
            v-bind:key="answer.id"
            v-bind:answer_props="answer"
            v-bind:id_current_user="id_current_user"
            @set_is_answered="set_is_answered"
            @remove_answer="remove_answer"/>

        <button  v-if="next_page" class="btn-load_more btn btn-success" v-on:click="load_more()">Load More</button>
    </div>  
</template>

<script>
    import Answer from '@/components/Answer';
    import DateMixin from '@/mixins/Date';
    import APIRequest from '@/common/api_request';

    export default {
        name: 'QuestionDetail',
        mixins: [DateMixin],
        components: {
			Answer
		},
        data: function () {
            return {
                answer_textarea : "",
                created_date : "",
                question_data : {},
                answer_data : [],
                next_page: "",
                error_api: "",
                is_author: false,
                is_answered: false,
                link_ask_question : {
                    name: 'action-question', 
                    params: {
                        action_question: "edit",
                        question_prop: null
                    }
                },
                id_current_user : 0,
                is_answering : false
            }
        }, 
        props: {
            question : Object,
        },
        created() {
            document.title = this.$route.params.question_title;

            if(this.question)
            {
                this.question_data = this.question;
                this.keep_created();
            }
            else{
                const url_api = "http://localhost:8000/api/questions-title/"+this.$route.params.question_title+"/";
                const apiRequest = new APIRequest(url_api)
                apiRequest.call_api().then((data) => {
                    if(apiRequest.get_response_status() == 404)
                        this.$router.push({ name: 'page-not-found'});
                    else{
                        this.question_data = data;
                        this.keep_created();
                    }
                });
            }
        },
        mounted() {
            
        },
        methods: {
            submit_answer(){
                const post_data = { 
                    answer: this.answer_textarea,
                    question: this.question_data.id
				}
                const url_api = "http://localhost:8000/api/answers/";
                new APIRequest(url_api, 'POST', post_data).call_api().then((data) => {
                    this.answer_data.unshift(data);
                });
            },
            set_is_answered(value) {
				this.is_answered = value;
			},
            set_is_answering(value){
                this.is_answering = value;
            },
            remove_answer(_id){
                this.answer_data = this.question_data.answer;
                for (var i = 0; i < this.answer_data.length; i++){
                    if(this.answer_data[i].id == _id) {
                        this.answer_data.splice(i, 1);
                        this.is_answered = false;
                    }
                }
            },
            delete_question(){
                const url_api = "http://localhost:8000/api/questions/"+this.question_data.id+"/";
                const apiRequest = new APIRequest(url_api, 'DELETE');
                apiRequest.call_api().then((data) => {
                    if(apiRequest.get_response_status() == 401){
                        this.error_api = data;
                        setTimeout(() => this.error_api = false, 5000);
                    }
                    else{
                        this.$router.push({ name: 'home'});
                    }
                });
            },
            keep_created(){
                this.question_data.created_date = this.format_date_question(this.question_data.created)
                this.link_ask_question.params.question_prop = this.question_data;
                this.api_is_author();
                //this.answer_data = this.question_data.answer;
                const url_api = "http://localhost:8000/api/questions/"+this.$route.params.question_title+"/answers/";
                this.call_api_answer(url_api);
            },
            api_is_author(){
                const url_api = "http://localhost:8000/api/users/me/";
                new APIRequest(url_api).call_api().then((data) => {
					if(data.username == this.question_data.author_name)
                        this.is_author = true;

                    this.id_current_user = data.id;
                });
            },
            call_api_answer(url_api){
				new APIRequest(url_api).call_api().then((data) => {
                    this.answer_data.push(...data.results);
                    this.next_page = data.next;
				});
            },
            load_more() {
				this.call_api_answer(this.next_page);
            }
        },
    }
</script>

<style scoped>
	.question {
        cursor: auto;
    }
    .container-button-answer
    {
        margin: 10px 0;
        padding: 10px 0;
        border-top: 1px solid #ccc;
        border-bottom: 1px solid #ccc;
    }
    .container-answering{
        background: #f5f5f5;
        padding: 15px;
        border: 1px solid #dadada;
        border-radius: 5px;
    }
    .container-answering textarea{
        width: 100%;
        padding: 8px;
        border-radius: 2px;
    }
    .container-answering textarea::placeholder{
        color: #ccc;
    }
</style>
