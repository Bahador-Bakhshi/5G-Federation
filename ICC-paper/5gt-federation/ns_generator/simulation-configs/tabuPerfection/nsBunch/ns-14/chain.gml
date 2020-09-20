graph [
  node [
    id 0
    label 1
    disk 10
    cpu 3
    memory 15
  ]
  node [
    id 1
    label 2
    disk 1
    cpu 1
    memory 5
  ]
  node [
    id 2
    label 3
    disk 2
    cpu 2
    memory 11
  ]
  node [
    id 3
    label 4
    disk 6
    cpu 2
    memory 9
  ]
  node [
    id 4
    label 5
    disk 6
    cpu 2
    memory 1
  ]
  node [
    id 5
    label 6
    disk 9
    cpu 4
    memory 8
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 32
    bw 50
  ]
  edge [
    source 0
    target 1
    delay 29
    bw 160
  ]
  edge [
    source 0
    target 2
    delay 30
    bw 119
  ]
  edge [
    source 0
    target 3
    delay 34
    bw 113
  ]
  edge [
    source 1
    target 5
    delay 33
    bw 124
  ]
  edge [
    source 2
    target 4
    delay 31
    bw 174
  ]
]
