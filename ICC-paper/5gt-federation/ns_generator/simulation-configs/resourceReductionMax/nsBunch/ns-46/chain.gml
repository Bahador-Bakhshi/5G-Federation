graph [
  node [
    id 0
    label 1
    disk 5
    cpu 1
    memory 16
  ]
  node [
    id 1
    label 2
    disk 4
    cpu 1
    memory 6
  ]
  node [
    id 2
    label 3
    disk 10
    cpu 2
    memory 11
  ]
  node [
    id 3
    label 4
    disk 1
    cpu 2
    memory 11
  ]
  node [
    id 4
    label 5
    disk 6
    cpu 4
    memory 3
  ]
  node [
    id 5
    label 6
    disk 2
    cpu 1
    memory 10
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 29
    bw 66
  ]
  edge [
    source 0
    target 1
    delay 33
    bw 156
  ]
  edge [
    source 0
    target 2
    delay 35
    bw 82
  ]
  edge [
    source 1
    target 3
    delay 26
    bw 57
  ]
  edge [
    source 2
    target 5
    delay 33
    bw 158
  ]
  edge [
    source 3
    target 4
    delay 32
    bw 80
  ]
]
