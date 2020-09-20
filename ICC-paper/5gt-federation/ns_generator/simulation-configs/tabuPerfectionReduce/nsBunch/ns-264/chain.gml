graph [
  node [
    id 0
    label 1
    disk 3
    cpu 3
    memory 4
  ]
  node [
    id 1
    label 2
    disk 10
    cpu 1
    memory 3
  ]
  node [
    id 2
    label 3
    disk 5
    cpu 1
    memory 1
  ]
  node [
    id 3
    label 4
    disk 10
    cpu 2
    memory 16
  ]
  node [
    id 4
    label 5
    disk 8
    cpu 1
    memory 11
  ]
  node [
    id 5
    label 6
    disk 3
    cpu 4
    memory 4
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 30
    bw 152
  ]
  edge [
    source 0
    target 1
    delay 31
    bw 196
  ]
  edge [
    source 1
    target 2
    delay 32
    bw 115
  ]
  edge [
    source 2
    target 3
    delay 25
    bw 57
  ]
  edge [
    source 2
    target 4
    delay 33
    bw 122
  ]
  edge [
    source 3
    target 5
    delay 34
    bw 62
  ]
]
