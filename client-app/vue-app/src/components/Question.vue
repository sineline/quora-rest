<template>
	<main>
        <li class="question">
            <p class="author">Posted by <span>{{ question.author }}</span></p>
            <p class="title">{{ question.title }}</p>
            <p class="answer">Answers: {{ question.answer.length }}</p>
        </li>
  	</main>
</template>

<script>
export default {
	name: 'Question',
	data: function () {
        return {
            //questions : []
        }
	}, 
  	props: {
        question : Object,
  	},
  	mounted() {
		
	},
	methods: {
		
	},
}
</script>

<style scoped>
	.question{
        list-style-type: none;
        text-align: left;
    }
    .author{
        
    }
    .title{
        
    }
    .answer{
        
    }
</style>
