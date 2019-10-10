<script>
    export default {
        name: 'DateMixin',
        data: function () {
            return {
            }
        },
        methods: {
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