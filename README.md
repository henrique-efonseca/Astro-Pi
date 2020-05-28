# Astro Pi - Team cos(π)

<b> Astro Pi - Mission Space Lab 2018/2019 </b> <br>
<b> Team name: </b> cos(π) - Coding of Space <br>
<b> Professor:</b> M. Cristina Pinho <br>
<b> Students:</b> <br>
<ul>
<li> David Afonso <br>
<li> David Dantas <br>
<li> David Nabeiro <br>
<li> <a href="https://github.com/henrique-efonseca"> Henrique Fonseca </a> <br>
<li> Rodrigo Estrela <br>
<li> Tomás Carvalho<br>
</ul>
<b> School: </b> Escola Secundária Sebastião e Silva<br>
<b> City:</b> Oeiras <br>
<b> Country:</b> Portugal <br>
<br>


# Introduction
"_The European Astro Pi Challenge is an ESA Education project run in collaboration with the Raspberry Pi Foundation. It offers young people the amazing opportunity to conduct scientific investigations in space by writing computer programs that run on Raspberry Pi computers aboard the International Space Station (ISS)_." <br>
<br>
"_Mission Space Lab offers students and young people the chance to have their scientific experiments run on the ISS. Your challenge is to design and program an experiment to be run on an Astro Pi computer. The best experiments will be deployed to the ISS, and your team will have the opportunity to analyse your results and put together a short report about your findings. The ten teams that write the best reports will be selected as the Astro Pi Mission Space Lab winners_!"<br>
<br>

# Mission Resume
The main objective of the experiment is to study the relativity of the movement between a two-body system. We intend to demonstrate the validity of Galileo's Theory of Relativity, from an experimental point of view, using the Raspberry Pi. Using a mathematical model deducted, we used the photographs of the Earth among their coordinates to calculate the relative velocity and prove the importance of the Galileo's Theory of Relativity in experiments with this type of systems.  As a secondary mission, we used the Humidity, Pressure and Temperature sensors to turn the RaspberryPi into a Human-Presence detector. We have also used be data science methods to find the experimental error associated with the AstroPi device.
<br>
<br>

 
# Code
Our Algorithm has a run-time of approximately 3 hours (2 ISS orbits).
Functions of our Algorithm:

```python
    def security():
        """
        Function to get data from the environment on the ISS and compare it to
        the referenced values. This is used to check if anyone is near
        the AstroPi and to set colors and messages on the Sense Hat
        depending on Human Presence.
        """
    
    def get_Lat_Lon():
        """
        Function to get the latitude and longitude values
        from the 'ephem' library and write them to EXIF data for the
        photographys.
        """
    
   def photography():
        """
        Function to take photographs every 5 seconds.
        """
    
    def data():
        """
        Function to read the data gathered by the Raspberry Pi and store it in designated log file.
        """
    
    def MainFunction():
        """
        Function to run all the other functions in a multi-threading procedure.
        """  
```


<br>

# Images
Example of the images we used for calculating the relative velocity:

![20x20 grid](https://github.com/henrique-efonseca/Astro-Pi/blob/master/Photographs/coscodingofspace_photo_0654.jpg)

<br>

# Files   
 <b> Files description: </b> <br>
  <ul>
    <li> <a href="https://github.com/henrique-efonseca/AstroPi/blob/master/main.py"> main.py</a> - Code of the project. <br>
 <li> <a href="https://github.com/henrique-efonseca/AstroPi/blob/master/Report.pdf"> Report.pdf</a> - Final report of the experiment. <br>
    <li> <a href="https://github.com/henrique-efonseca/AstroPi/blob/master/Data01.csv"> Data01.csv</a> - File with raw data collected.  <br>
    <li> <a href="https://github.com/henrique-efonseca/AstroPi/blob/master/Data02.csv"> Data02.csv</a> - File with raw data collected.  <br>
    <li> <a href="https://github.com/henrique-efonseca/AstroPi/blob/master/Log-Files.log"> Log-Files.log</a> - File with the logs of the program.  <br>
    <li> <a href="https://github.com/henrique-efonseca/AstroPi/tree/master/Photographs"> Photographs</a> - Folder with some photographs taken with the Astro Pi.  <br>  
   </ul>
   <br>
   
   
# Special Thanks </b> <br>
  <ul>
    <li> M. Cristina Pinho - Our Professor and Mentor for this project, for all the support.<br>
    <li> Francisco Santos - Professor at Instituto Superior Técnico, for his scientific review of the experiment. <br>
    <li> <a href="https://github.com/afonsocrg">Afonso Gonçalves</a> - Our friend, for his help reviewing the code.    <br>
 </ul>
   <br>
   

# Mission Space Lab Informations
<li> https://astro-pi.org/missions/space-lab/ </li>



