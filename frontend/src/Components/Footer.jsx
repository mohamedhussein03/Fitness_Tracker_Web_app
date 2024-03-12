import React from 'react'
import {FaFacebook ,FaTiktok ,FaInstagram , FaVoicemail} from 'react-icons/Fa'
const Footer = () => {
  return (
    <div name='contact' className='w-full h-50'>
        <div className='flex flex-col justify-center items-center w-full h-full'>
            <div className='max-w-[1000px] w-full grid grid-cols-2 gap-8'>
            <div className='pb-8 pl-4'>
                <h1 className='text-4xl font-bold  inline border-b-4 text-[#bd4c72] border-[#250e15]'> 
            Contact :
            </h1>
            </div>
            <div></div>
            
            </div>
            <div className='max-w-[1000px] w-full grid sm:grid-cols-2 gap-8 px-4'>
       
            <div className='sm:text-right text-xl font-bold'>
                <p className='flex items-center'> Email <FaVoicemail className='m-2' />:</p>
                </div>
            <div className='sm:text-right text-xl font-bold'>
                <p className='flex items-center'> Instagram  <FaInstagram className='m-2' />:</p>
                </div>
            <div className='sm:text-right text-xl font-bold'>
                <p className='flex items-center'> TikTok <FaTiktok className='m-2' />:</p>
                </div>
            <div className='sm:text-right text-xl font-bold'>
                <p className='flex items-center'> Facebook <FaFacebook className='m-2' />:</p>
                </div>

            </div>
        </div>
    </div>
  )
}

export default Footer