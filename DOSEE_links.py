#
#	DOSEE_links.py
#
#	Opens links to help with Divinity Original Sin: Enhanced Edition (DOSEE) sessions
#	Links contain info on:
#		Crafting Table
#		Skill Descriptions 
#		Skill Book Merchant Locations
#		
#	Shunman Tse									Dec. 2016
#	Version: 0.1
#

import os, sys, webbrowser

# Links List
links_to_open = [\
"http://www.seth-dehaan.com/divinity_crafting/",\
"http://divinityoriginalsin.wiki.fextralife.com/Skills",\
"http://www.oldgames.sk/docs/Divinity-Original-Sin/merchants.php"]

# main
#	Opens each link in a new tab
def main():
	
	for link in links_to_open:
		webbrowser.open_new_tab (link)
	
main()