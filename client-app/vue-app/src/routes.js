import Register from './components/Register.vue';
import Login from './components/Login.vue';
import Home from './components/Home.vue';


const routes = [
    { name: 'home', path: '/', component: Home },
    { name: 'register', path: '/register', component: Register },
    { name: 'login', path: '/login', component: Login },
];

export default routes;