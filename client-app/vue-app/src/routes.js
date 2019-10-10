import Register from './views/Register.vue';
import Login from './views/Login.vue';
import Home from './views/Home.vue';
import QuestionEdit from './views/QuestionEdit.vue';
import QuestionDetail from './views/QuestionDetail.vue';
import AnswerEdit from './views/AnswerEdit.vue';

const routes = [
    { name: 'home', path: '/', component: Home },
    { name: 'action-question', path: '/question/:action_question', component: QuestionEdit, props: true },
    { name: 'register', path: '/register', component: Register },
    { name: 'login', path: '/login', component: Login },
    { name: 'answer-edit', path: '/answer/:id_answer', component: AnswerEdit, props: true},
    { name: 'question-detail', path: '/:question_title', component: QuestionDetail, props: true },
];

export default routes;