<script>
    export default {
        name: 'QuestionLinkMixin',
        data: function () {
            return {
            }
        },
        methods: {
            createLinkQuestion: function (_question) {
                return {
                    name: 'question-detail', 
                    params: { 
                        question_title: _question.url_title,
                        question : _question
                    }, 
                }
            }
        },
    }

</script>