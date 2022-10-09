# DungeonmasterSuperstore
A website that gives users space to create magical items for their Dungeons and Dragon campaigns. Backend with Django and Frontend with Bootstrap5 stored in a Docker container.


I started learning about Django after spending months with Python. Having no background in web development and learning a new framework was extremely difficult, which made me want to challenge myself and make something substantial. The plan was to create a space for dungeon masters to showcase their own magical items for their players, it was something that meant alot to me as it coupled both my passions; coding and dungeons and dragons. 

The features of the website are:
1. A complete custom Auth system.
2. User created items that can be updated. 
3. A custom URL for users to display their items.
4. Ability to view other users URL's and a master list of total items created.
5. Edit/update user account information. 


The design:

I used different models for each type of item (weapons, armor, etc) but realized half-way through developement that I could have used a singular model and used Forms to gather the specific data. This would have cut down on the numerous views and URLS but I believe it would have been harder for someone to follow the design process. I decided to keep the current model system due to future updates and clearer code. 

Creating accounts for just the dungeon master and not all users was always the design idea. Visitors to the website should be able to access all the items created by all the users, this gives players and dungeon masters the ability to share their creations and inspire their creativity. 

Future features of the website:
1. Search function
2. Click-to-link URL for easy sharing

The website was an amazing challnge for me, it pushed me to learn new concepts and grow to meet the demands of what I had envisioned. The learning curve was steep but it gave me such an appreciation for Django and how powerful it is. I'm excited to continue working on DungeonmasterSuperstore and other future projects. 
