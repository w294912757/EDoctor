import Vue from 'vue'
import VueRouter from "vue-router"

import Main from "../components/windows/basic/Main"
import SignUp from "../components/windows/basic/SignUp";
import Login from "../components/windows/basic/Login";
import Default from "../components/windows/basic/Default";
import Clinics from "../components/windows/visitor/Clinics";
import Doctors from "../components/windows/visitor/Doctors";
import ClinicDetail from "../components/windows/visitor/detail/ClinicDetail";
import DoctorDetail from "../components/windows/visitor/detail/DoctorDetail";
import ClinicApplyMenu from "../components/windows/root/ClinicApplyMenu";
import DoctorApplyMenu from "../components/windows/root/DoctorApplyMenu";
import ClinicApplyDetail from "../components/windows/root/apply/ClinicApplyDetail";
import DoctorApplyDetail from "../components/windows/root/apply/DoctorApplyDetail";
import CreatePrescription from "../components/windows/doctor/CreatePrescription";
import AllPrescriptions from "../components/windows/doctor/AllPrescriptions";
import PrescriptionDetail from "../components/windows/doctor/PrescriptionDetail";
import Clinic2Doctors from "../components/windows/clinic/Clinic2Doctors";
import Clinic2Prescriptions from "../components/windows/clinic/Clinic2Prescriptions";

Vue.use(VueRouter)
const originalPush = VueRouter.prototype.push

VueRouter.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(err => err)

}

const routes = [
  {
    path: '/',
    component: Main,
    children: [
      {
        path: '/login',
        name: 'login',
        component: Login,
      }, {
        path: '/signup',
        name: 'signup',
        component: SignUp,
      }, {
        path: '/default',
        name: 'default',
        component: Default,
      }, {
        path: '/clinics',
        name: 'clinics',
        component: Clinics,
      }, {
        path: '/clinicdetail',
        name: 'clinicdetail',
        component: ClinicDetail
      }, {
        path: '/doctors',
        name: 'doctors',
        component: Doctors,
      }, {
        path: '/doctordetail',
        name: 'doctordetail',
        component: DoctorDetail
      }, {
        path: '/clinicapplymenu',
        name: 'clinicapplymenu',
        component: ClinicApplyMenu
      }, {
        path: '/doctorapplymenu',
        name: 'doctorapplymenu',
        component: DoctorApplyMenu
      }, {
        path: '/clinicapplydetail',
        name: 'clinicapplydetail',
        component: ClinicApplyDetail
      }, {
        path: '/doctorapplydetail',
        name: 'doctorapplydetail',
        component: DoctorApplyDetail
      }, {
        path: '/createprescription',
        name: 'createprescription',
        component: CreatePrescription
      }, {
        path: '/allprescriptions',
        name: 'allprescriptions',
        component: AllPrescriptions
      }, {
        path: '/prescriptiondetail',
        name: 'prescriptiondetail',
        component: PrescriptionDetail
      }, {
        path: '/clinic2prescriptions',
        name: 'clinic2prescriptions',
        component: Clinic2Prescriptions
      }, {
        path: '/clinic2doctors',
        name: 'clinic2doctors',
        component: Clinic2Doctors
      }
    ]
  }
]


const router = new VueRouter({
    routes: routes,
  }
)

export default router


