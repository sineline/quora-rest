<template>
	<div class="hello">
		<img alt="Vue logo" src="../assets/logo.png">
		<h1>Share your knowledge!</h1>
		<form v-on:submit.prevent>
			<label for="username-input">Username</label>
			<input type="text" name="username" id="username-input" v-model="username" autocomplete="username">
			<br>
			<label for="password-input">Password</label>
			<input type="password" name="password" id="password-input" v-model="password_val" autocomplete="current-password">
			<p><button v-on:click="callLoginApi()">Login</button></p>
			<p>Or <router-link to='/register'>Create a new account</router-link></p>
		</form>
	</div>
</template>

<script>
import APIRequest from '@/common/api_request'
export default {
	name: 'Login',
	data: function () {
		return {
			username: '',
			password_val: '',
		}
	},  
	props: {
		msg: String,
	},
	mounted() {
			
	},
	methods: {
		callLoginApi() {
			const post_data = { 
				username: this.username,
				password: this.password_val
			}
			
			const url_api = "http://localhost:8000/api/token-auth/";
			new APIRequest(url_api, 'POST', post_data).call_api().then((data) => {
				// We say to App that it is loggued to display header
				localStorage.token = data.token;
				this.$emit('setIsLoggued', true); 
				
				this.$router.push({ name: 'home'});
			});
		},
	},
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
	h3 {
		margin: 40px 0 0;
	}
	ul {
		list-style-type: none;
		padding: 0;
	}
	li {
		display: inline-block;
		margin: 0 10px;
	}
	a {
		color: #42b983;
	}
</style>
