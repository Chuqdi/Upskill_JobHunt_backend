import Image from "next/image";

// Aos Animation
import AOS from "aos";
import "aos/dist/aos.css";

//React
import {useEffect} from 'react'

//Image
import upskillTv from '../../../images/upskill-Tv.png';
import upskill from '../../../images/upskill-network.png'
import harriet from '../../../images/harriet.png';





const Sponsor = () => {

    useEffect(() => {
        AOS.init({ duration: 1500 });
      }, []);
    return(
        <section className="">
            <h1 className="text-center text-2xl font-semibold my-16">Meet our partners</h1>
            <div className="flex flex-col  justify-center my-8 bg-slate-800" data-aos="zoom-in">
                <Image
                    src={upskill}
                    width={300}
                height={200}
                alt="upskill-logo"
                />
                <div className="lg:pt-24 pt-12 pl-4 md:pl-10 ">
                    <Image
                        src={harriet} 
                        width={300}
                        height={200}
                        alt="harriet-logo"
                    />
                </div>
                <div>
                <Image
                    src={upskillTv}
                    width={400}
                height={200}
                alt="upskilltv-logog"
                />
                </div>
            </div>
        </section>
    )
}

export default Sponsor;