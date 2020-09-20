graph [
  node [
    id 0
    label 1
    disk 6
    cpu 4
    memory 2
  ]
  node [
    id 1
    label 2
    disk 6
    cpu 4
    memory 5
  ]
  node [
    id 2
    label 3
    disk 7
    cpu 1
    memory 2
  ]
  node [
    id 3
    label 4
    disk 4
    cpu 2
    memory 2
  ]
  node [
    id 4
    label 5
    disk 8
    cpu 1
    memory 1
  ]
  node [
    id 5
    label 6
    disk 10
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
    delay 29
    bw 80
  ]
  edge [
    source 0
    target 1
    delay 27
    bw 156
  ]
  edge [
    source 1
    target 2
    delay 33
    bw 70
  ]
  edge [
    source 2
    target 3
    delay 31
    bw 191
  ]
  edge [
    source 2
    target 4
    delay 25
    bw 165
  ]
  edge [
    source 2
    target 5
    delay 25
    bw 95
  ]
]
