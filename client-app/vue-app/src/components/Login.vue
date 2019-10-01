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
export default {
	name: 'Login',
	data: function () {
		return {
			username: '',
			password_val: '',
			token: ''
		}
	},  
  	props: {
		msg: String,
  	},
  	mounted() {
		// fetch("https://jsonplaceholder.typicode.com/users")
		// 	.then(response => response.json())
		// 	.then((data) => {
		// 		this.users = data;
		// 	})
		if(localStorage.token) 
			this.token = localStorage.token;
	},
	methods: {
		callLoginApi() {
			const post_date = { 
				username: this.username,
				password: this.password_val
			}
			
			//console.debug(this.data.username);
			fetch("http://localhost:8000/api/token-auth/", {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify(post_date)
			})
			.then(response =>response.json())
			.then((data) => {
				//this.posts = data;
				console.debug(data.token);
				this.token = data.token;
				localStorage.token = this.token;
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
