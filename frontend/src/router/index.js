import Vue from 'vue'
import VueRouter from "vue-router"

import MainWindow from "../components/windows/basic/MainWindow"
import SignUpWindow from "../components/windows/basic/SignUpWindow";
import LoginWindow from "../components/windows/basic/LoginWindow";
import DefaultWindow from "../components/windows/basic/DefaultWindow";
import ClinicsWindow from "../components/windows/visitor/ClinicsWindow";
import DoctorsWindow from "../components/windows/visitor/DoctorsWindow";
import ClinicDetailWindow from "../components/windows/visitor/ClinicDetailWindow";
import DoctorDetailWindow from "../components/windows/visitor/DoctorDetailWindow";

Vue.use(VueRouter)
const originalPush = VueRouter.prototype.push

VueRouter.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(err => err)

}

const routes = [
  {
    path: '/',
    component: MainWindow,
    children: [
      {
        path: '/loginwindow',
        name: 'loginwindow',
        component: LoginWindow,
      }, {
        path: '/signupwindow',
        name: 'signupwindow',
        component: SignUpWindow,
      }, {
        path: '/defaultwindow',
        name: 'defaultwindow',
        component: DefaultWindow,
      }, {
        path: '/clinicswindow',
        name: 'clinicswindow',
        component: ClinicsWindow,
      }, {
        path: '/clinicdetailwindow',
        name:'clinicdetailwindow',
        component: ClinicDetailWindow
      }, {
        path: '/doctorswindow',
        name: 'doctorswindow',
        component: DoctorsWindow,
      }, {
        path: '/doctordetailwindow',
        name: 'doctordetailwindow',
        component: DoctorDetailWindow
      }
    ]
  }
]


const router = new VueRouter({
    routes: routes
  }
)

export default router


