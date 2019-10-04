<template>
    <div class="question container-main">
        <h2 class="title-question">{{ question_data.title }}</h2>
        <button class="btn btn-outline-success" >Edit</button>
        <button class="btn btn-outline-danger" v-on:click="delete_question()">Delete</button>
        <div class="alert alert-danger" role="alert" v-if="error_api">{{ error_api }}</div>
        <p class="author">Posted by <span>{{ question_data.author_name }}</span></p>
        <p class="created">{{ question_data.created_date }}</p>
    </div>  
</template>

<script>
export default {
	name: 'QuestionDetail',
	data: function () {
        return {
            created_date : "",
            question_data : "",
            error_api: ""
        }
	}, 
  	props: {
        question : Object,
    },
    created() {
        if(this.question)
        {
            this.question_data = this.question;
            this.question_data.created_date = this.format_date_question(this.question_data.created)
        }
        else{
            fetch("http://localhost:8000/api/questions-title/"+this.$route.params.question_title+"/", {
                method: 'GET',
                headers: {
                    'Authorization': 'Token '+localStorage.token
                },
            })
            .then(response => response.json())
            .then((data) => {
                this.question_data = data;
                this.question_data.created_date = this.format_date_question(this.question_data.created)
            });
        }
    },
  	mounted() {
        
    },
	methods: {
		async delete_question(){
            try {
                const response = await fetch("http://localhost:8000/api/questions/"+this.question_data.id+"/", {
                    method: 'DELETE',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': 'Token '+localStorage.token
                    },
                });

                const response_status = await response.status;
                if(response_status == 401){
                    this.error_api = await response.json();
                    setTimeout(() => this.error_api = false, 5000);
                }
                else{
                    this.$router.push({ name: 'home'});
                }
            } catch (error) {
                console.error('Error:', error);
            }
        },
        format_date_question(_created_date){
            const options = { year: 'numeric', month: 'long', day: 'numeric' };
            const array_date = _created_date.split("-");
            const created_date =  new Date(array_date[0], array_date[1], array_date[2])
        
            const created_date_str = created_date.toLocaleDateString("en-US", options);
            return created_date_str.replace(/,/g, "");
        }
	},
}
</script>

<style scoped>
	
</style>
