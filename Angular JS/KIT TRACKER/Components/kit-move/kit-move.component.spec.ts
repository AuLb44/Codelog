import { ComponentFixture, TestBed } from '@angular/core/testing';

import { KitMoveComponent } from './kit-move.component';

describe('KitMoveComponent', () => {
  let component: KitMoveComponent;
  let fixture: ComponentFixture<KitMoveComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [KitMoveComponent]
    });
    fixture = TestBed.createComponent(KitMoveComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
