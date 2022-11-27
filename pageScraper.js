const puppeteer = require('puppeteer');
const fs = require("fs/promises")

const start = async (url) => {
	try {
	//   console.log(`starting ${url}`)
		const browser = await puppeteer.launch()
		const page = await browser.newPage()
		await page.goto(url)
  
		const selector = '.sizeOrigin'
		await page.waitForSelector(selector)
		const links = await page.$$eval(selector, am => am.filter(e => e.href).map(e => e.href))
		
		const names = await page.evaluate(() => {
		return Array.from(document.querySelectorAll(".yregion")).map(x => x.textContent)
	})
		const names2 = await page.evaluate(() => {
		return Array.from(document.querySelectorAll(".info.title")).map(x => x.textContent)
	})
	
		await fs.writeFile("pastvu-data.txt", names + ',' +  names2 + '\n', {'flag':'a'})
		await fs.writeFile("pastvu-links.txt", links + '\n', {'flag':'a'})
		await fs.writeFile("links-order.txt", url + '\n', {'flag':'a'})
		// console.log(links)
		console.log(url)

		await browser.close()
	} catch (err) {
	  console.log(err)
	}
  }
  
// start("https://pastvu.com/p/236800")
// start("https://pastvu.com/p/144873")
// start("https://pastvu.com/p/130639")
// start("https://pastvu.com/p/130640")
// start("https://pastvu.com/p/1455152")
// start("https://pastvu.com/p/139985")
// start("https://pastvu.com/p/150201")
// start("https://pastvu.com/p/134825")

// start("https://pastvu.com/p/134823")
// start("https://pastvu.com/p/271842")
// start("https://pastvu.com/p/1028206")
// start("https://pastvu.com/p/271838")
// start("https://pastvu.com/p/134822")
// start("https://pastvu.com/p/134821")
// start("https://pastvu.com/p/1028202")
// start("https://pastvu.com/p/271836")

// start("https://pastvu.com/p/1631361")
// start("https://pastvu.com/p/115389")
// start("https://pastvu.com/p/804234")
// start("https://pastvu.com/p/636229")
// start("https://pastvu.com/p/134555")
// start("https://pastvu.com/p/600146")
// start("https://pastvu.com/p/768410")
// start("https://pastvu.com/p/1313747")

// start("https://pastvu.com/p/115385")
// start("https://pastvu.com/p/115386")
// start("https://pastvu.com/p/115387")
// start("https://pastvu.com/p/600246")
// start("https://pastvu.com/p/600248")
// start("https://pastvu.com/p/1026531")
// start("https://pastvu.com/p/1026532")

// start("https://pastvu.com/p/115383")
// start("https://pastvu.com/p/120900")
// start("https://pastvu.com/p/702286")
