import AuthContext from '../../../../context/auth-context';
import Calender from './Calander';
import {useContext} from 'react';

import { faClose} from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';



const LeftSideDrawer = ({open, close}) => {

    const {week, setWeek} = useContext(AuthContext)
    return(
        <>{open ? <section className="fixed top-0 left-0  w-full z-40 overflow-y-scroll lg:hidden" style={{backgroundColor:'rgba(0, 0, 0, 0.774)'}}>
        <div className="bg-white  w-96 overflow-y-scroll ml-auto lsd_anime">
        <section className=" h-screen pt-5  lg:block" >
        <FontAwesomeIcon icon={faClose} className="m   text-green-600 text-2xl mx-3" onClick={close}/>
        <div className="flex justify-between bg-white">
              <h1 className="text-2xl ml-8">Henry Truth</h1>
              <div className="bg-slate-700 h-14 w-14 rounded-full mr-4 ">
              </div>
            </div>
             <Calender weeks={"Week 1"} weekroute={"Week1"}/>
             <Calender weeks={"Week 2"} weekroute={"Week2"}/>
         </section>
        </div>
    </section>: null}</>
    )
}

export default LeftSideDrawer;