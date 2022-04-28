import { faBook} from '@fortawesome/free-solid-svg-icons';
import { faBriefcase} from '@fortawesome/free-solid-svg-icons';
import { faPerson} from '@fortawesome/free-solid-svg-icons';
import { faMoneyBill} from '@fortawesome/free-solid-svg-icons';
import { faClose} from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import Link from "next/link";


const RightSideDrawer = ({open, close}) => {

    return(
       <>{open ? <section className="fixed top-0 left-0  w-full z-40 overflow-y-scroll lg:hidden " style={{backgroundColor:'rgba(0, 0, 0, 0.774)'}}>
       <div className="bg-white  w-56 overflow-y-scroll rsd_anime">
       <section className=" h-screen pt-5  lg:block" >
       
           <FontAwesomeIcon icon={faClose} className="ml-48 mb-8  text-green-600 text-2xl mx-3" onClick={close}/>
           <Link href="/"><h1 className="text-xl font-bold ml-2 mb-8 text-center">Owerri <span className="font-bold " style={{color:"#14A800"}} >JobHunt</span></h1></Link>

       <div>
           <Link href="#">
               <div className="my-4 flex py-2 mx-4  text-lg text-white mr-2 rounded-md shadow-xl cursor-pointer" style={{backgroundColor:"#14A800"}} >
               <FontAwesomeIcon icon={faPerson} className="ml-6 mt-1"/>
               <h1 className="ml-4">DashBoard</h1>
           </div>
       </Link>
       <Link href="/dashboard/candidate/course">
           <div className="my-4 flex py-2 mx-4 text-lg text-white mr-2 rounded-md shadow-xl cursor-pointer" style={{backgroundColor:"#14A800"}} >
               <FontAwesomeIcon icon={faBook} className="ml-6 mt-1"/>
               <h1 className="ml-4">My Courses</h1>
           </div>
       </Link>
       <Link href="/dashboard/candidate/jobs">
           <div className="my-4 py-2 flex mx-4 text-center text-lg text-white mr-2 rounded-md shadow-xl cursor-pointer"  style={{backgroundColor:"#14A800"}} >
               <FontAwesomeIcon icon={faBriefcase} className="ml-6 mt-1"/>
               <h1 className="ml-4">My jobs</h1>
           </div>
       </Link>
       <Link href="#">
           <div className="mt-8 flex mx-4 py-8 text-center text-lg text-white mr-2 rounded-md shadow-xl cursor-pointer"  style={{backgroundColor:"#14A800"}}>
               <FontAwesomeIcon icon={faMoneyBill} className="ml-6 mt-1"/>
               <h1 className="pl-2">Make Payment</h1>
           </div>
       </Link>
       <button className="bg-white py-4 mx-auto my-4 text-green-500 font-semibold shadow-xl px-6 mx-10 border rounded-md">Logout</button>
       </div>

   </section>
       </div>
   </section>: null}</>
    )
}

export default RightSideDrawer;