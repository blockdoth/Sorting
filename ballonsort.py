#TODO:
#Comprese the gif after its finsched to reduce file size

#===[IMPORTS]===#
import matplotlib.pyplot as plt #For making plots
import numpy as np #Dunno but cant use without
import random #For random list
import os # To make and edit folders
import shutil #To delete folders with contents
import imageio # To make a gif from the plots

lenlist=256  # Sets the amount of items in the list
unsorted = random.sample(range(0,lenlist), lenlist) #Makes a list with random numbers as long as lenlist

#===[FUNCTIONS]===#
def swap(list,pos1,pos2): # swap to items in list
    get = list[pos1], list[pos2] #MAGIC
    list[pos2], list[pos1] = get #MAGIC doesn't work when get= is before list[pos1] and list[pos2]
    return list #Returns list with swapped items

def bubbel_sort(list):#The bubble sort algoritme
    sortedvar = True #Setss sortedvar tot True 
    color = 0 #Sets the id of the bar that should be red to 0
    for i in range(len(list)): #Loop as long as the length of the list
            if i + 1< len(list): #Prevents an error
                x = list[i] #Get id of first element
                y = list[i+1] #Get id of second element
                if x > y: # Compares the first element en tests if its bigger then te second
                    color = x #Collects the id of the first element to turn it red later
                    sortedvar = False # If  element 1 is bigger then element 2 it means the list is not yet sorted
                    list = swap(list,i,i+1) #Swaps the elements if element 1 is bigger then element 2
    
    return list, sortedvar, color #Returns the slightly sorted list, if its sorted and the id of the highsest sorted element

def make_dir(name): #Folder maker
    name = name + str(lenlist)#Makes a name for the folder based on te length of the list
    script_dir = os.path.dirname(__file__)#Defines the location of the main file of the script
    new_dir = os.path.join(script_dir, name)#Defines the path for the new folder
    if os.path.isdir(new_dir): #If there is already a folder with the same name present, remove it
        shutil.rmtree(new_dir)
    os.makedirs(new_dir) #Make an new folder with at the correct location
    return new_dir # Returns the location of the new folder


def sort(list):
    it = 1 #Sets start point
    save_loc_list = [] #Creates list for the locations
    s = list # Sets the x-axis  as the list
    t = np.arange(0.0, len(list), 1) #Set the y-axis as 
    results_dir = make_dir("Results_len_list_") #Makes a folder and set its location as a var
    
    while True: #Make a never ending loop
        plt.cla() #Clears the plot
        sorting_alg = bubbel_sort(list) #Runs the function and assignes its results to a var
        s = sorting_alg[0] # Sets the x-axis as the list
        bar_list = plt.bar(s,t) # Makes a bar plot
        bar_list[sorting_alg[2]].set_color('r') # sets the id of the highest sorted item to red
        plt.xticks([]) #removes labels on the x-axis
        plt.yticks([]) #removes labels on the y-axis
        plt.title("Iteration: {x}".format(x=it)) # Gives the plot a titkle and the current iteration   
        save_loc = "{y}/test{x}.png".format(y=results_dir,x=it) # Sets the location where the plot should be saved and names it after the length of the list
        it = it + 1 #Move to the next iteration
        
        if sorting_alg[1] == True:#Breaks the never ending loop if the sorting algorimte returns True for sorted
            print('Done') #Print in termanial to let you know its finished
            break #Exists the loop
        save_loc_list.append(save_loc) #Appends the save location to a list of save locations for all the iterations
        plt.savefig(save_loc) #Save it to the assigned location
        
    return save_loc_list #Returns the list with the save locations of all the plots

#===[THE PROGRAM]===#
frames_path = sort(unsorted) #Runs the function and assignes its results to a var
gif_path = make_dir("Result_gif_len_")+"/Result_gif_len_"+str(lenlist)+".gif" # Makes a folder for the gif made from all the plots and names it after the length of the sorted list

with imageio.get_writer(gif_path,mode='I') as writer: #Collects all the paths to all the plots
    for i in range(len(frames_path)): #Loop as long as the save_loc_list has elements
        writer.append_data(imageio.imread(frames_path[i])) #Makes a frame in the .gif from each plot

