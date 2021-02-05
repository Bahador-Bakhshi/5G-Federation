graph [
  node [
    id 0
    label 1
    disk 10
    cpu 2
    memory 6
  ]
  node [
    id 1
    label 2
    disk 2
    cpu 2
    memory 14
  ]
  node [
    id 2
    label 3
    disk 6
    cpu 3
    memory 9
  ]
  node [
    id 3
    label 4
    disk 6
    cpu 3
    memory 2
  ]
  node [
    id 4
    label 5
    disk 4
    cpu 3
    memory 16
  ]
  node [
    id 5
    label 6
    disk 4
    cpu 1
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
    bw 59
  ]
  edge [
    source 0
    target 1
    delay 33
    bw 80
  ]
  edge [
    source 1
    target 2
    delay 33
    bw 107
  ]
  edge [
    source 2
    target 3
    delay 29
    bw 62
  ]
  edge [
    source 2
    target 4
    delay 32
    bw 130
  ]
  edge [
    source 4
    target 5
    delay 35
    bw 64
  ]
]
