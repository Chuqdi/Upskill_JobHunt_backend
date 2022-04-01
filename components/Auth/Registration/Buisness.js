import Link from "next/link";
import { useState } from "react";
import { useRouter } from "next/router";
import Select from 'react-select';
import 'react-phone-number-input/style.css'
import PhoneInput from 'react-phone-number-input'


const Buisness = () => {

    const options = [
        { value: 'Techonlogy and Media', label: 'Techonlogy and Media' },
        { value: 'Food and Eatery', label: 'Food and Eatery' },
        { value: 'Industrial Services', label: 'Industrial Services' },
        { value: 'Health', label: 'Health' },
    ]

    const [selectedOption, setSelectedOption] = useState(null);
    const [phoneNumber, setPhoneNumber] = useState(undefined)

    const router = useRouter()

    const [buisness, setBuisness] = useState({
        buisnessName:'',
        buisnessEmail:'',
        buisnessPhoneNumber:'',
        buisnessType:'',
        businessPassword:'',
        confirmBuisnessPassword:'',
        buisnessNameError:'',
        buisnessEmailError:'',
        buisnessPhoneNumberError:'',
        buisnessTypeError:"",
        buisnessPasswordError:"",
        confirmBuisnessPasswordError:""


    })
    console.log(selectedOption, phoneNumber)

    const submitHandler = (e) => {
        e.preventDefault()

        buisness.buisnessName.length < 1 && 
        buisness.buisnessEmail.length < 1 && 
        phoneNumber === undefined && 
        selectedOption === null &&
        buisness.businessPassword.length < 1 && 
        buisness.confirmBuisnessPassword < 1 ? 
        setBuisness({...buisness, buisnessNameError:'Please input Buisness Name', buisnessEmailError:'Please input Buisness Email', buisnessPhoneNumberError:'Please input Buisness PhoneNumber', buisnessTypeError:'Please input BuisnessType', buisnessPasswordError:'Please input Buisness Password', confirmBuisnessPasswordError:'Please input confirm buisness password'}) : router.push('/email-verification/buisness')
        
    }

    return(
        <section className="py-48 w-full flex">
            <form className="flex flex-col mx-auto justify-center rounded-md shadow-xl w-96 px-4 border-2">
            <h1 className="text-center my-5 font-semibold" style={{color:"#14A800"}}>REGISTER AS A BUISNESS</h1>
                <div className="py-4 w-full ">
                    <label>Buisness Name</label>
                    <input  className="h-10 w-full outline-none border mt-4 border-green-500 pl-2 rounded-md" onChange={(e) => setBuisness({...buisness, buisnessName:e.target.value})}/>
                    <p className="text-red-600">{buisness.buisnessNameError}</p>
                </div>
                <div className="py-4 ">
                    <label>Buisness Email</label>
                    <input className="h-10 w-full outline-none border mt-4 border-green-500 pl-2 rounded-md" onChange={(e) => setBuisness({...buisness, buisnessEmail:e.target.value})}/>
                    <p className="text-red-600">{buisness.buisnessNameError}</p>
                </div>
                <div className="py-4 ">
                    <label>Buisness PhoneNumber</label>
                    <PhoneInput
                    placeholder="Enter phone number"
                    className="h-10 w-full outline-none border mt-4 border-green-500 pl-2 rounded-md" 
                    value={phoneNumber}
                    onChange={setPhoneNumber}/>
                    <p className="text-red-600">{buisness.buisnessPhoneNumberError}</p>
                </div>
                <div className="py-4 ">
                    <label>Buisness Type</label>
                    <Select
                        defaultValue={selectedOption}
                        onChange={setSelectedOption}
                        options={options}
                        className="h-10 w-full outline-none border mt-4 border-green-500 pl-2 rounded-md"
                    />
                    <p className="text-red-600">{buisness.buisnessTypeError}</p>

                </div>
                <div>
                    <label>Password</label>
                    <input className="h-10 w-full outline-none border mt-4 border-green-500 pl-2 rounded-md" type='password' onChange={(e) => setBuisness({...buisness, businessPassword:e.target.value})}/>
                    <p className="text-red-600">{buisness.buisnessPasswordError}</p>
                </div>
                <div>
                    <label>Confirm Password</label>
                    <input className="h-10 w-full outline-none border mt-4 border-green-500 pl-2 rounded-md" type='password' onChange={(e) => setBuisness({...buisness, confirmBuisnessPassword:e.target.value})}/>
                    <p className="text-red-600">{buisness.confirmBuisnessPasswordError}</p>
                </div>
                    <button className="w-48 mx-auto h-12 text-white rounded-full my-6 text-lg" onClick={submitHandler} style={{backgroundColor:"#14A800"}}>Sign Up</button>
                    <div className="flex">
                        <h1 className="py-2 pr-1 " style={{color:"#14A800"}}>Already have an account ?</h1>
                        <Link href="/buisness/login">
                            <span className="py-2 underline cursor-pointer" style={{color:"#14A800"}}>Log in</span>
                        </Link>
                    </div>
            </form>
        </section>
    )
    
}

export default Buisness;

