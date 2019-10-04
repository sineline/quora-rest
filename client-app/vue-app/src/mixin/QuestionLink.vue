<script>
    export default {
        name: 'QuestionLinkMixin',
        data: function () {
            return {
            }
        },
        methods: {
            // Lowercase - Remove Puntuation - replace space
            createLinkQuestion: function (_question) {
                return {
                    name: 'question-detail', 
                    params: { 
                        //question_title: _question.title.toLowerCase().replace(/[^\w\s]/gi, '').replace(/ /g,"_"),
                        question_title: _question.url_title,
                        question : _question
                    }, 
                }
            }
        },
    }

</script>