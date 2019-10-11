<template>
    <header>
        <div class="container-main container-header">
            <router-link class="title-site" to='/'>Question Time</router-link>
            <div class="container-button">
                <router-link class="btn btn-success" to='/'>Home</router-link>
				<router-link class="btn btn-danger" :to="link_ask_question">Ask a question</router-link>
                <button class="btn btn-light" v-on:click="logout()">Logout</button>
            </div>
        </div>
    </header>
</template>

<script>
	export default {
		name: 'Header',
		data: function () {
			return {
				link_ask_question : {
					name: 'action-question', 
					params: {action_question: "ask"}
				}
			}
		},
		mounted() {
			
		}, 
		props: {
		},
		methods: {
			logout() {
                localStorage.token = false;
                this.$emit('setIsLoggued', false);
                this.$router.push({ name: 'login'});
			},
        },
	}
</script>

<style>
	body #app {
		margin-top: 0px;
	}
    .container-main{
		width: 80vw;
		margin:auto;
	}
</style>
<style scoped>
	header{
		background: #f6f6f6;
		width: 100vw;
		padding: 10px;
	}
	.container-header{
		display: inline-grid;
		grid-template-columns: auto auto; 
	}
	header .title-site{
		justify-self: start;
		align-self: center;
		font-size: 29px;
		color: #3c3c3c;
	}
	header .container-button{
		justify-self: end;
	}
	header .container-button .btn{
		margin: 0 2px;
	}
	
</style>
