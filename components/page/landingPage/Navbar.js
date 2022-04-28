import Image from "next/image";
import Link from "next/link";

//Image
import hambuger from "../../../images/menu.png";
import close from "../../../images/close.png";

import { useEffect, useState } from "react";
import {
  CHECK_BUSINESS_SLUG_EXISTS,
  CHECK_USER_SLUG_EXISTS,
} from "../../../misc/helpers/authTokenManager";
import { useRouter } from "next/router";

const NavBar = () => {
  const router = useRouter();

  const [userLoggedIn, setUserLoggedIn] = useState(false);

  useEffect(() => {
    (CHECK_USER_SLUG_EXISTS() || CHECK_BUSINESS_SLUG_EXISTS()) &&
      setUserLoggedIn(true);
  }, [router.events]);

  const [open, setOpen] = useState(false);

  return (
    <>
      <nav className="bg-white flex flex-col lg:flex-row py-4 fixed w-full z-20 overflow-hidden">
        <div className="flex">
          <Link href="/">
            <h1 className="lg:text-4xl text-3xl font-bold ml-2 ">
              Owerri{" "}
              <span className="font-bold " style={{ color: "#14A800" }}>
                JobHunt
              </span>
            </h1>
          </Link>

          {open ? (
            <div
              className="ml-auto mr-4 cursor-pointer lg:hidden"
              onClick={() => setOpen((prev) => !prev)}
            >
              <Image src={close} alt="info" width={30} height={30} />
            </div>
          ) : (
            <div
              className="ml-auto mr-4 cursor-pointer lg:hidden"
              onClick={() => setOpen((prev) => !prev)}
            >
              <Image src={hambuger} alt="info" width={40} height={40} />
            </div>
          )}
        </div>

        <ul className="hidden ml-auto lg:flex lg:text-lg lg:mr-16 font-semibold">
          <Link href="/">
            <li className="mx-3 hover:text-green-700">
              <a href="">Home</a>
            </li>
          </Link>
          <li className="mx-3 hover:text-green-700">
            <a href="#services">Services</a>
          </li>
          <li className="mx-3 hover:text-green-700">
            <a href="#about-us">About Us</a>
          </li>
          <li className="mx-3 hover:text-green-700">
            <a href="#testimonials">Testimonials</a>
          </li>
          <li className="mx-3 hover:text-green-700">
            <a href="#contact-us">Contact Us</a>
          </li>

          {userLoggedIn ? (
            <Link href="/dashboard/candidate">
              <button
                className="flex text-white px-4 pt-1 rounded-md mr-8"
                style={{ backgroundColor: "#3C8224" }}
              >
                Dashboard
              </button>
            </Link>
          ) : (
            <Link href="/login">
              <button
                className="flex text-white px-4 pt-1 rounded-md mr-8"
                style={{ backgroundColor: "#3C8224" }}
              >
                Login
              </button>
            </Link>
          )}
        </ul>
        {open && (
          <div className="h-44 text-black my-6  ">
            <ul className=" flex flex-col text-lg lg:mr-16 font-bold text-md ">
              <Link href="/">
                <li
                  className="mx-3 hover:text-green-700"
                  onClick={() => setOpen((prev) => !prev)}
                >
                  <a href="">Home</a>
                </li>
              </Link>
              <li
                className="mx-3 hover:text-green-700"
                onClick={() => setOpen((prev) => !prev)}
              >
                <a href="#services">Services</a>
              </li>
              <li
                className="mx-3 hover:text-green-700"
                onClick={() => setOpen((prev) => !prev)}
              >
                <a href="#about-us">About Us</a>
              </li>
              <li
                className="mx-3 hover:text-green-700"
                onClick={() => setOpen((prev) => !prev)}
              >
                <a href="#testimonials">Testimonials</a>
              </li>
              <li
                className="mx-3 hover:text-green-700"
                onClick={() => setOpen((prev) => !prev)}
              >
                <a href="#contact-us">Contact Us</a>
              </li>
              <Link href="/login">
                <button
                  className="flex  text-white px-4 pt-1 rounded-md w-24 ml-2 h-10 pt-2 "
                  onClick={() => setOpen((prev) => !prev)}
                  style={{ backgroundColor: "#3C8224" }}
                >
                  Login
                </button>
              </Link>
            </ul>
          </div>
        )}
      </nav>
    </>
  );
};

export default NavBar;
