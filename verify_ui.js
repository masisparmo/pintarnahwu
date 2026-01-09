const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch({ args: ['--no-sandbox'] });
  const page = await browser.newPage();

  // Load the local HTML file
  const filePath = 'file://' + path.resolve('index.html');
  await page.goto(filePath);

  console.log('Page loaded');

  // Check if button exists
  const button = page.getByText('Tulis Arab');
  if (await button.isVisible()) {
      console.log('Button "Tulis Arab" found');
  } else {
      console.error('Button "Tulis Arab" not found');
      process.exit(1);
  }

  // Click button and check modal
  await button.click();
  const modal = page.locator('#drawing-modal');
  if (await modal.isVisible()) {
      console.log('Modal opened');
  } else {
      console.error('Modal did not open');
      process.exit(1);
  }

  // Check canvas
  const canvas = page.locator('#draw-canvas');
  if (await canvas.isVisible()) {
      console.log('Canvas is visible');
  } else {
      console.error('Canvas not found');
      process.exit(1);
  }

  // Check toolbar buttons
  const undoBtn = page.locator('button[title="Undo"]');
  const redoBtn = page.locator('button[title="Redo"]');
  const clearBtn = page.locator('button[title="Hapus Semua"]');

  if (await undoBtn.isVisible() && await redoBtn.isVisible() && await clearBtn.isVisible()) {
      console.log('Toolbar buttons found');
  } else {
      console.error('Toolbar buttons missing');
  }

  // Close modal
  await page.getByText('Batal').click();
  if (!await modal.isVisible()) {
      console.log('Modal closed');
  } else {
      console.error('Modal did not close');
  }

  await browser.close();
})();
