<template>
    <div class="answer">
        <!-- <router-link> -->
            <p class="top-answer"><span class="author_name">{{ answer_data.author_name }}</span> - <span class="author_updated">{{ answer_updated }}</span></p>
            <h3 class="title-answer">{{ answer_data.answer }}</h3>
            <button class="like_answer btn" 
                    v-bind:class="{ 'btn-danger': is_liked, 'btn-outline-danger': !is_liked }" 
                    v-on:click="like_answer()"
                    v-if="!is_owner_answer">
                Like ({{ answer_data.like.length }})
            </button>
            <div v-if="is_owner_answer">
                <router-link 
                    class="btn btn-outline-secondary" 
                    :to="{name: 'answer-edit', params: {id_answer: answer_data.id, answer: answer_data}}">
                    Edit
                </router-link>
                <button class="btn btn-outline-danger" v-on:click="delete_answer()">
                    Delete
                </button>
            </div>
        <!-- </router-link> -->
    </div>
</template>

<script>
    import DateMixin from '../mixins/Date.vue';

    export default {
        name: 'Answer',
        mixins: [DateMixin],
        data: function () {
            return {
                answer_updated : "",
                is_liked : 0,
                answer_data : Object,
                is_owner_answer: false
            }
        }, 
        props: {
            answer_props : Object,
            id_current_user : Number,
        },
        watch: {
            // whenever id_current_user changes, this function will run
            id_current_user: function () {
                this.set_id_current_user();
            }
        },
        created() {
            this.answer_updated = this.format_date_question(this.answer_props.updated);
            this.answer_data = this.answer_props;
            this.set_id_current_user(); 
        },
        mounted() {

        },
        methods: {
            delete_answer(){
                const url_api = "http://localhost:8000/api/answers/"+this.answer_data.id+"/";
                const apiRequest = new APIRequest(url_api, 'DELETE').call_api().then((data) => {
                    if(apiRequest.get_response_status() != 401){
                        this.$emit('remove_answer', this.answer_data.id);
                    }
                });
            },
            set_id_current_user(){
                for(const like of this.answer_data.like) {
                    if(like.liker == this.id_current_user)
                    {
                        this.is_liked = like.id;
                        break;
                    }
                }

                if(this.answer_data.author == this.id_current_user){
                    this.$emit('set_is_answered', true);
                    this.is_owner_answer = true;
                }
            },
            async like_answer(){
				const post_data = { 
                    answer: this.answer_props.id,
                    like: this.is_liked ? false : true,
                }
                
                const url_api = (this.is_liked)
					? "http://localhost:8000/api/likes/"+this.is_liked+"/"
                    : "http://localhost:8000/api/likes/";
                
                const method = this.is_liked ? 'DELETE' : 'POST';
                const apiRequest = new APIRequest(url_api, method).call_api().then((data) => {
                    if(apiRequest.get_response_status() == 201){
                        this.answer_data.like.push(data);
                        this.is_liked = data.id;
                    }
                    else{ // DELETE
                        //console.error(this.answer_data.like);
                        for (var i = 0; i < this.answer_data.like.length; i++){
                            if(this.answer_data.like[i].id == this.is_liked) {
                                this.answer_data.like.splice(i, 1);
                                this.is_liked = 0;
                            }
                        }
                    }
                });
            },
        },
    }
</script>
<style>
	
    
</style>

<style scoped>
    .author_updated{
        color: #999;
    }
    .answer{
        padding: 20px 0;
        border-bottom: 1px solid #ccc;
    }
</style>
