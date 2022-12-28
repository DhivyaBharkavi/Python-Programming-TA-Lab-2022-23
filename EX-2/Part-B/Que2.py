"""
Five Star Video rents new videos for $3.00 a night and oldies for $2.00 a night.
Write a program that the clerks at Five Star Video can use to calculate the total charge for a customer’s video rentals.
The program should prompt the user for the number of each type of video and output the total cost.
"""
new_videos = int(input("Enter the no of new videos "))
cost_of_new_video = int(input("Enter the cost of new video "))
old_videos = int(input("Enter the no of old videos "))
cost_of_old_video = int(input("Enter the cost of old video "))
total_cost = (new_videos * cost_of_new_video) + (old_videos * cost_of_old_video)
print("Total cost of videos is ",total_cost)
