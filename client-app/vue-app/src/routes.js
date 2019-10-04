import Register from './components/Register.vue';
import Login from './components/Login.vue';
import Home from './components/Home.vue';
import AskQuestion from './components/AskQuestion.vue';
import QuestionDetail from './components/QuestionDetail.vue';

const routes = [
    { name: 'home', path: '/', component: Home },
    { name: 'ask-question', path: '/ask-question', component: AskQuestion },
    { name: 'register', path: '/register', component: Register },
    { name: 'login', path: '/login', component: Login },
    { name: 'question-detail', path: '/:question_title', component: QuestionDetail, props: true },
];

export default routes;