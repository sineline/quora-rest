import Register from './views/Register.vue';
import Login from './views/Login.vue';
import Home from './views/Home.vue';
import QuestionEdit from './views/QuestionEdit.vue';
import QuestionDetail from './views/QuestionDetail.vue';
import AnswerEdit from './views/AnswerEdit.vue';
import NotFound from './views/NotFound.vue';

const routes = [
    { name: 'home', path: '/', component: Home },
    { name: 'action-question', path: '/question-action/:action_question', component: QuestionEdit, props: true },
    { name: 'register', path: '/register', component: Register },
    { name: 'login', path: '/login', component: Login },
    { name: 'answer-edit', path: '/answer/:id_answer', component: AnswerEdit, props: true},
    { name: 'question-detail', path: '/question/:question_title', component: QuestionDetail, props: true },
    { name: 'page-not-found', path: '*', component: NotFound},
];

export default routes;