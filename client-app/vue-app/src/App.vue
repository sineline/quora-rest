<style>
  #app {
	  font-family: serif;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      text-align: center;
      color: #2c3e50;
      margin-top: 60px;
  }
</style>
<style>
  @import 'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css';
</style>
<template>
  <div id="app">
    <Header v-if="is_loggued" @setIsLoggued="setIsLoggued"/>
    <router-view @setIsLoggued="setIsLoggued"/>
  </div>
</template>

<script>
	import Header from './components/Header.vue';
	  
  	export default {
      	name: 'App',
		components: {
			Header
		},
		data: function () {
			return {
				is_loggued : (localStorage.token && localStorage.token != "false") ? true : false,
			}
		},
		mounted() {

		},
		methods: {
			setIsLoggued (value) {
				console.log("set_is_loggued:"+value);
				this.is_loggued = value;
			}
		}
  }
</script>


