<style>
	#app {
		font-family: serif;
		-webkit-font-smoothing: antialiased;
		-moz-osx-font-smoothing: grayscale;
		text-align: center;
		color: #2c3e50;
		margin-top: 60px;
	}
  	.fade-enter-active, .fade-leave-active {
		transition: opacity .2s;
	}
	.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
		opacity: 0;
	}
</style>
<style>
  @import 'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css';
</style>

<template>
  <div id="app">
    <Header v-if="is_loggued" @setIsLoggued="setIsLoggued"/>
	<transition name="fade">
    	<router-view @setIsLoggued="setIsLoggued"/>
	</transition>
  </div>
</template>

<script>
	import Header from './components/Header';
	  
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
				this.is_loggued = value;
			}
		}
  }
</script>


