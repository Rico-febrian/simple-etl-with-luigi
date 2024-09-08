from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError
import asyncio

async def main():
    """
    This function used to scrapes data from the selected website saved the HTML content.
    
    """
    # Set the playwright context manager    
    async with async_playwright() as playwright:
        
        # Initialize the browser variable
        browser = None
        try:
            
            # Launch the Chromium browser in headless mode
            browser = await playwright.chromium.launch(headless=False, slow_mo=50)
            
            # Open a new page/tab in the browser
            page = await browser.new_page()
            
            # Set the url from selected website 
            url = 'https://best.aliexpress.com/?spm=a2g0o.tm1000008654.logo.1.39d76f3dkeodMY&browser_redirect=true'

            # Access the web page and wait until it is fully loaded
            await page.goto(url, wait_until='networkidle', timeout=60000)

            # Set up the selector
            # Configure the selector to change the location
            ship_to_selector = '#_full_container_header_23_ > div.pc-header--right--2cV7LB8 > div > div.pc-header--items--tL_sfQ4 > div.es--wrap--RYjm1RT > div:nth-child(1) > div'
            
            # Set form content selector to fill the location input 
            form_content_selector = '#_full_container_header_23_ > div.pc-header--right--2cV7LB8 > div > div.pc-header--items--tL_sfQ4 > div.es--wrap--RYjm1RT > div.es--contentWrap--ypzOXHr.es--visible--12ePDdG > div:nth-child(2) > div > div.select--text--1b85oDo'
            
            # Set the input locator to fill the selected location. In this project, 'USA' is selected
            fill_input = '#_full_container_header_23_ > div.pc-header--right--2cV7LB8 > div > div.pc-header--items--tL_sfQ4 > div.es--wrap--RYjm1RT > div.es--contentWrap--ypzOXHr.es--visible--12ePDdG > div:nth-child(2) > div > div.select--popup--W2YwXWt.select--visiblePopup--VUtkTX2 > div.select--search--20Pss08 > input'  
            
            # Select "USA" from the country selector and click
            usa_input = '#_full_container_header_23_ > div.pc-header--right--2cV7LB8 > div > div.pc-header--items--tL_sfQ4 > div.es--wrap--RYjm1RT > div.es--contentWrap--ypzOXHr.es--visible--12ePDdG > div:nth-child(2) > div > div.select--popup--W2YwXWt.select--visiblePopup--VUtkTX2 > div:nth-child(3)'
            
            # Set the save button selector to save the location change
            save_button = '#_full_container_header_23_ > div.pc-header--right--2cV7LB8 > div > div.pc-header--items--tL_sfQ4 > div.es--wrap--RYjm1RT > div.es--contentWrap--ypzOXHr.es--visible--12ePDdG > div.es--saveBtn--w8EuBuy'

            try:
                # Click on the "Ship to" selector
                await page.click(ship_to_selector)
                
                # Click on the form content selector and wait for the fill input to be available
                await page.click(form_content_selector, timeout=60000)
                await page.wait_for_selector(fill_input)

                # Fill the location input with 'United States'
                await page.fill(fill_input, 'United States')
                await page.click(usa_input)

                # Wait a moment to ensure the "United States" option appears
                await asyncio.sleep(2)

                # Click the save button to confirm the location change
                await page.click(save_button)

                # Wait for the page to reload and ensure it is fully loaded
                await page.wait_for_load_state('networkidle')

                print("Successfully changed 'Ship to' to United States")
            except PlaywrightTimeoutError:
                print("Unable to change 'Ship to' settings. Proceeding with current settings.")

            # Set the item selector to load a main content
            item_selector = '#more-to-love > div.water-fall--water-fall--1mDxCdm.water-fall--same-height--3qZeF-a > div:nth-child(1)'
            
            # Wait until the main content is loaded
            await page.wait_for_selector(item_selector, timeout=60000)

            # looping until no more content can be loaded
            while True:
                
                # Scroll down several times and wait for more content to load
                for _ in range(5):
                    await page.evaluate('window.scrollBy(0, window.innerHeight)')
                    await asyncio.sleep(2)

                # Try to click the "Load More" button if it exists
                next_page_button_selector = '#more-to-love > div:nth-child(3) > div'
                try:
                
                    # Wait for the "Load More" button to appear
                    await page.wait_for_selector(next_page_button_selector, timeout=10000)
                    
                    # Click the "Load More" button to load additional content
                    await page.click(next_page_button_selector)
                    await asyncio.sleep(5)
                except PlaywrightTimeoutError:
                    
                    # If the "Load More" button is not found or already at the end of the page, print a message and break the loop
                    print('No "Load More" button found or already at the end of the page.')
                    break
                
            # Save the scraped HTML content to a file
            html_content = await page.content()
            with open('scraping_output/ali-express-scrape-us.html', 'w', encoding='utf-8') as file:
                file.write(html_content)
            
            print('HTML content saved successfully!')
            
        except PlaywrightTimeoutError:
            print("Timeout waiting for page to load. Check your internet connection or the website might be down.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
             # Close the browser if it was opened
            if browser:
                await browser.close()

# Run the function
asyncio.run(main())