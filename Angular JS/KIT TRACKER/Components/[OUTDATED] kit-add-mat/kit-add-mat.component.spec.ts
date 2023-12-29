import { ComponentFixture, TestBed } from '@angular/core/testing';

import { KitAddMatComponent } from './kit-add-mat.component';

describe('KitAddMatComponent', () => {
  let component: KitAddMatComponent;
  let fixture: ComponentFixture<KitAddMatComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [KitAddMatComponent]
    });
    fixture = TestBed.createComponent(KitAddMatComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
