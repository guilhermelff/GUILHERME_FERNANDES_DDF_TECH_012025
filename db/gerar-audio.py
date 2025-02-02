# Import the required module for text 
# to speech conversion
from gtts import gTTS

# This module is imported so that we can 
# play the converted audio
import os

# The text that you want to convert to audio
mytext = """AeroClean 3000
An innovative air purifier with advanced filtering technology and intelligent control for healthier environments.

EcoSmart Thermostat
A state-of-the-art thermostat that adapts to your routine, optimizing energy consumption and providing comfort.

Quantum Drone
A high-tech drone with advanced artificial intelligence, perfect for capturing precise aerial images.

VibeSound Speaker
A high-fidelity sound system delivering immersive audio with deep bass and crystal-clear highs.

FlexiCharge Wireless
A wireless charger compatible with multiple devices, offering fast and secure charging.

ProVision 4K Monitor
A 27-inch monitor with ultra-high definition resolution, perfect for designers, professionals, and gamers.

SonicBreeze Fan
A quiet and energy-efficient fan with multiple speeds and adjustable control for ideal cooling.

UltraFit Smartwatch
A modern smartwatch that monitors your health, tracks physical activities, and seamlessly integrates with your devices.

SmartLock Pro
A digital lock system with biometric authentication and remote access, ensuring security and convenience.

PureH2O Filter
A water filtration system that ensures a safe and healthy water supply, with easy installation and maintenance.

TravelMate Luggage
A robust yet lightweight travel suitcase equipped with GPS tracking and smart compartments for better organization.

Speedster Electric Scooter
A high-performance electric scooter with a long-lasting battery and smooth acceleration, perfect for urban traffic.

ZenBrew Coffee Maker
An intuitive coffee maker offering various brewing options, ensuring the perfect cup for every taste.

PixelPerfect Camera
A compact digital camera with advanced sensors and AI-powered image processing, ideal for both amateur and professional photographers.

TerraTech Solar Panel
Efficient solar panels designed to maximize energy capture even in low-light conditions.

AquaFlow Shower
A modern shower system with adjustable pressure and temperature control, providing a luxurious bathing experience.

GigaDrive SSD
A high-speed solid-state drive with large storage capacity and enhanced data security.

SyncStation Hub
A versatile docking station that connects multiple devices and offers fast data transfer rates.

Nebula VR Headset
A virtual reality headset that provides immersive experiences with high-resolution visuals.

OptiClear Glasses
Lightweight and stylish glasses with anti-glare technology and blue light filtering for enhanced visual comfort.

EcoWash Dishwasher
An energy-efficient dishwasher that cleans your dishes using minimal water.

SmartFarm Irrigation
An automated irrigation system that monitors soil moisture and optimizes water usage in agriculture.

TurboCharge Battery
A portable power bank with fast charging, ideal for keeping your devices powered on the go.

FitTrack Scale
An intelligent scale that provides detailed body composition metrics and syncs with health apps.

SecureNet Router
A high-speed router with advanced security features and continuous connectivity for your home network.

NanoClean Vacuum
A compact and powerful vacuum cleaner designed to efficiently clean various residential spaces.

GlamGlow Mirror
An intelligent mirror with adjustable lighting and virtual makeup tutorials for a flawless look.

AquaPure Humidifier
A stylish humidifier that improves indoor air quality, operating silently and consistently.

Solaire Lantern
A rechargeable LED lantern with multiple brightness settings, perfect for outdoor adventures.

HomeHub Assistant
A voice-controlled home assistant that integrates and manages all the connected devices in your home.

LightWave Bulbs
Energy-efficient LED bulbs with adjustable brightness and color temperature to create the perfect ambiance.

ActivePulse Earbuds
Wireless earbuds with crisp sound and a secure fit, ideal for sports and everyday use.

UrbanRide Bike
An electric bike with a modern design, perfect for urban commuting with long battery life.

CrystalClear Projector
A portable projector that transforms any space into a cinema room with vibrant and sharp images.

MicroPrint 3D Printer
A compact 3D printer, ideal for creating prototypes and detailed designs in the comfort of your home.

DataVault Cloud
A secure cloud storage solution offering continuous backup and advanced data protection.

GameForge Console
A next-generation gaming console with ultra-fast loading times and immersive graphics for an incredible experience.

PureTone Microphone
A professional microphone that ensures clear audio capture, perfect for podcasts, streaming, and studio recordings.

AeroDesk Standing
An adjustable standing desk designed to improve posture and boost productivity at work.

ZenGarden Planter
A smart planter that monitors plant health and automates irrigation for a consistently vibrant garden.

OptiCharge Cable
A robust and fast charging cable compatible with various devices for added convenience.

AquaLux Showerhead
A luxurious showerhead with multiple spray patterns, offering a spa-like bathing experience.

TurboBlend Mixer
A powerful blender that mixes, crushes, and processes food with ease, perfect for the modern kitchen.

Visionary Projector
A high-definition projector, ideal for corporate presentations and home cinema sessions.

FusionSound Bar
A sleek soundbar that delivers rich, immersive audio, transforming your living room into a true cinema.

EcoDrive Car Charger
An efficient car charger designed to rapidly charge devices during your journey.

SmartScribe Pen
A digital pen that converts handwritten notes into digital text, making idea storage and sharing easier.

AirGlide Hoverboard
A futuristic hoverboard with advanced gyroscopic technology for smooth and fun transportation.

PowerPulse Fitness Tracker
A comprehensive fitness tracker that accurately monitors heart rate, steps, and sleep patterns.

GigaStream Router
A next-generation router that provides ultra-fast speeds and a stable connection, ideal for connected environments.

SmartSip Bottle
A smart bottle that tracks your water intake and sends reminders to keep you hydrated throughout the day.

Lumina LED Strip
A flexible LED strip with customizable colors and remote control, perfect for decorating and lighting up spaces.

PulseBeat Smartwatch
A smartwatch that monitors physical activities, tracks health, and provides real-time notifications.

EcoChill Refrigerator
A highly energy-efficient refrigerator with advanced cooling technology and smart storage.

VisionPro Eyewear
Modern eyewear with augmented reality features for navigation and quick access to information.

MegaSound Headphones
Over-ear headphones with noise cancellation, providing an immersive and comfortable audio experience.

QuickFix Toolkit
A versatile, high-quality toolkit, ideal for professionals and DIY enthusiasts.

SolarSync Charger
An eco-friendly solar charger that lets you recharge devices anywhere using solar energy.

AeroMax Drone
A high-performance drone with advanced stabilization and a high-resolution camera for aerial photos and videos.

OptiFlex Keyboard
An ergonomic wireless keyboard with customizable backlighting, perfect for long typing sessions.

SmartShade Blinds
Automated blinds that adjust according to sunlight and indoor temperature, optimizing comfort.

VividView Monitor
A vibrant and responsive monitor, ideal for gamers and professionals demanding high graphical performance.

EcoVibe Speaker
A portable Bluetooth speaker made from eco-friendly materials, combining modern design with excellent sound quality.

PrimeCharge Power Bank
A robust power bank with fast charging capacity and multiple USB ports for enhanced flexibility.

InstaPrint Photo Printer
A portable photo printer that produces high-quality prints directly from your smartphone.

AirPure Mask
A reusable mask with an advanced filtration system, ensuring purer air and effective protection.

ProTone Guitar
An electric guitar with a modern design and exceptional sound quality, perfect for musicians of all levels.

SmartChef Oven
A connected oven that simplifies recipe preparation with precise temperature control and smart programs.

QuickBrew Kettle
An electric kettle with rapid heating, a safe design, and energy-saving features for your kitchen.

CityRide Scooter
A compact electric scooter designed for urban transportation with extended range and efficient performance.

PowerGlide Skates
Electric skates with adjustable speed settings and a robust build, ideal for urban adventures.

AeroFlex Backpack
A modern backpack with an ergonomic design and smart compartments for devices and accessories.

EcoStream Water Bottle
A reusable water bottle with a built-in filter, ensuring clean and sustainable hydration.

UltraDrive SSD
A high-speed SSD designed for gamers and professionals who demand quick access to their data.

SmartPulse Monitor
A medical digital oximeter offering accurate readings and integration with health apps for continuous monitoring.

VisionX VR Glove
An innovative glove for virtual reality experiences, providing tactile feedback for realistic immersion.

HomeWave Speaker
A smart speaker that connects to your home network and offers voice command audio control.

QuickCharge Adapter
A versatile power adapter that supports fast charging for a wide range of devices.

AquaSense Sensor
A smart sensor that monitors water quality and provides real-time analysis for safe consumption.

FusionFit Treadmill
A high-performance treadmill with interactive programs and real-time monitoring, ideal for intense workouts.

SonicStream Earbuds
Wireless earbuds with stable connectivity and superior sound clarity for daily use and sports.

EcoGuard Security
A residential security system with smart cameras, sensors, and remote monitoring for enhanced protection.

LumiGlow Lamp
A modern lamp with adjustable brightness and integrated USB ports, combining style and functionality.

AeroSense Air Monitor
A compact air quality monitor that tracks pollutants and provides recommendations for healthier environments.

SmartStitch Sewing
An advanced sewing machine with automatic functions, ideal for professionals and fashion enthusiasts.

UltraSound Baby Monitor
A baby monitor with high-definition audio and video, ensuring safety and peace of mind for parents.

FlexiFlow Water Pump
A durable water pump, suitable for both residential and commercial use, ensuring a constant and reliable flow.

PrimeStream Media Box
A compact streaming device that supports 4K video and high-fidelity audio for your living room.

CrystalCharge Dock
A sleek docking station with multiple ports for laptops and smartphones, streamlining your workspace organization.

OptiPrint Laser
A high-speed laser printer that delivers professional-quality prints, ideal for office environments.

SonicSurge Soundbar
A powerful soundbar that elevates your home cinema experience with dynamic sound and intense bass.

EcoLink Smart Plug
A smart plug that enables remote control of devices and energy consumption monitoring.

UrbanEdge E-Bike
A robust electric bike designed for urban traffic, combining modern design with high range.

LightPulse Fitness Band
A lightweight fitness band that monitors your daily activities and provides real-time health insights.

AeroStream Router
A high-performance router equipped with advanced features to ensure a stable and fast internet connection.

ProClean Steam Mop
A steam mop that efficiently cleans and sanitizes your floors, reducing the need for chemicals.

SmartGlide Iron
A smart iron with precise temperature control and anti-slip technology, ensuring always impeccable clothes.

QuickScan Document Scanner
A compact document scanner that digitizes documents quickly and in high resolution, making file organization easier.

FusionEdge Gaming Mouse
An ergonomic gaming mouse with programmable buttons and high precision, providing a competitive edge.

CrystalSound Home Theater
A complete home theater system that delivers immersive audio and impressive visuals for a cinematic experience at home."""

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("products.mp3")