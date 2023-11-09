INSERT INTO menu_items (name, description, price, spice_level, category_type_id, cuisine_type_id)
VALUES 
  ('Chicken and Waffles', 'Crispy fried chicken served on top of fluffy buttermilk waffles, drizzled with maple syrup and garnished with fresh herbs.', 12.99, 1, 2, 1),
  ('Breakfast Brisket Tacos', 'Soft corn tortillas filled with tender, slow-cooked brisket, scrambled eggs, sautéed onions, and bell peppers. Topped with salsa and avocado slices.', 10.49, 2, 2, 1),
  ('Beignets', 'Deep-fried dough pastries dusted with powdered sugar, served warm and fluffy. Perfectly crispy on the outside, light and airy on the inside.', 6.99, 1, 3, 1),
  ('Strawberry Cheesecake Pancakes', 'Fluffy pancakes filled with creamy cheesecake bites and fresh strawberry slices. Topped with whipped cream and a drizzle of strawberry sauce.', 9.99, 1, 2, 1),
  ('Bacon Stuffed Tots', 'Crispy tater tots stuffed with a savory mixture of bacon bits, cheddar cheese, and green onions. Served with a side of zesty ranch dipping sauce.', 8.49, 1, 1, 1),
  ('Hot Chocolate', 'Rich and creamy hot chocolate made with premium cocoa powder, steamed milk, and a dollop of whipped cream on top. Served piping hot for a comforting experience.', 4.99, 1, 4, 3),
  ('Mimosa', 'A classic brunch cocktail made with equal parts of sparkling wine and chilled citrus juice, usually orange juice. Served in a champagne flute and garnished with a fresh orange slice.', 7.99, 1, 4, 2);

ALTER TABLE "menu_items" ADD FOREIGN KEY ("category_type_id") REFERENCES "category_types" ("id");

ALTER TABLE "menu_items" ADD FOREIGN KEY ("cuisine_type_id") REFERENCES "cuisine_types" ("id");
