<template>
    <div class="question">
        <router-link :to="link_question">
            <p class="author">Posted by <span>{{ question.author_name }}</span></p>
            <h2 class="title">{{ question.title }}</h2>
            <p class="answer">Answers: {{ question.answer.length }}</p>
        </router-link>
    </div>
</template>

<script>
    import QuestionLinkMixin from '@/mixins/QuestionLink.vue';

    export default {
        name: 'Question',
        mixins: [QuestionLinkMixin],
        data: function () {
            return {
                link_question: {}
            }
        }, 
        props: {
            question : Object,
        },
        mounted() {
            this.link_question = this.createLinkQuestion(this.question);
        },
        methods: {
            
        },
    }
</script>
<style>
	.question{
        list-style-type: none;
        text-align: left;
        padding: 10px 0;
        border-bottom: 1px solid #dfdfdf;
        font-family: initial;
        cursor: pointer;
    }
    .question p{
        padding: 0;
        margin: 0;
        color: #555;
        font-weight: bold;
    }
    .author span{
        color: #ff4c4c;
    }
    .title{
        color: #1c1c1c;
        font-weight: bold;
    }
    
</style>

<style scoped>
    a:hover {
        color: auto;
        text-decoration: none;
    }
</style>
