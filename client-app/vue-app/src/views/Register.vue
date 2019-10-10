<template>
  	<div class="hello">
		<img alt="Vue logo" src="../assets/logo.png">
		<h1>Create your question time account!</h1>
		<h2 v-if="success">Bravo, you are going to be redirected!</h2>
		<form v-on:submit.prevent>
			<label for="username-input">Username</label>
			<input type="text" name="username" id="username-input" v-model="username" autocomplete="username">
			<br>
			<label for="email-input">Email Address*</label>
			<input type="email" name="email" id="email-input" v-model="email" autocomplete="email">
			<br>
			<label for="password-input">Password*</label>
			<input type="password" name="password" id="password-input" v-model="password" autocomplete="current-password">
			<br>
			<label for="password_confirmation-input">Password Confirmation*</label>
			<input type="password" name="password_confirmation" id="password_confirmation-input" v-model="password_confirmation" autocomplete="current-password">
			<p v-if="error_password">Please Same password</p>
			<p><button v-on:click="callApiCreateAccount()">Create Account</button></p>
			<div v-if="error_api" v-html=error_api></div>
			<p>Or <router-link to='/login'>Sign in instead</router-link></p>
		</form>

  	</div>
</template>

<script>
	import APIRequest from '../common/api_request'
	export default {
		name: 'Register',
		data: function () {
			return {
				username: '',
				email: '',
				password: '',
				password_confirmation: '',
				error_password: false,
				error_api: false,
				success: false
			}
		},  
		/*props: {
			msg: String,
		},*/
		methods: {
			callApiCreateAccount() {
				this.error_password = false;
				this.error_api = false;

				if(this.password != this.password_confirmation){
					this.error_password = true;
					return;
				}

				const post_date = { 
					username: this.username,
					email: this.email,
					password: this.password
				}

				const url_api = "http://localhost:8000/api/users/add/";
				const apiRequest = new APIRequest(url_api, 'POST', post_data);
				apiRequest.call_api().then((data) => {
					if(apiRequest.get_response_status() == 400)
					{
						this.error_api = "";
						for (var key in data) {
							this.error_api += "<p>About "+key+":"+data[key]+"</p>"
						}
					}
					else{
						this.success = true;
						setTimeout(() => this.$router.push({ name: 'login'}), 5000);
					}
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
