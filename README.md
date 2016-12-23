##Summary
I'd like to improve the **scalability** of a program that scrapes user-submitted page URLs and the citations found therein.

The challenge is to develop a script that **handles the io asynchronously**:

 1. Lookup of the source page
 2. Lookup of the cited pages
 3. Process the cited pages: 
 4. Save to DB
 5. Upload JSON to Amazon S3

What is the **optimal way of doing this** without making the code hard to read?

I would think that the average request time should be able to be shrunk down to less than 2 seconds if everything is asynchronous.

Currently **it takes over 10 seconds** and blocks, meaning that a 2-core CPU can do ~ 12 requests per minute.

I've included notes about libraries used in actual project in case you have any ideas about to **minimize memory usage**.

Also note that I intend to gather user submissions and process them in a queue like Celery and the user does not need to wait for the results.