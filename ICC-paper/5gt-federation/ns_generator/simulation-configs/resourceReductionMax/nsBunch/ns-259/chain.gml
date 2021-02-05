graph [
  node [
    id 0
    label 1
    disk 7
    cpu 3
    memory 16
  ]
  node [
    id 1
    label 2
    disk 10
    cpu 1
    memory 1
  ]
  node [
    id 2
    label 3
    disk 4
    cpu 4
    memory 1
  ]
  node [
    id 3
    label 4
    disk 8
    cpu 2
    memory 1
  ]
  node [
    id 4
    label 5
    disk 4
    cpu 4
    memory 12
  ]
  node [
    id 5
    label 6
    disk 1
    cpu 2
    memory 16
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 29
    bw 61
  ]
  edge [
    source 0
    target 1
    delay 35
    bw 168
  ]
  edge [
    source 1
    target 2
    delay 25
    bw 85
  ]
  edge [
    source 2
    target 3
    delay 35
    bw 196
  ]
  edge [
    source 3
    target 4
    delay 33
    bw 64
  ]
  edge [
    source 4
    target 5
    delay 33
    bw 176
  ]
]
