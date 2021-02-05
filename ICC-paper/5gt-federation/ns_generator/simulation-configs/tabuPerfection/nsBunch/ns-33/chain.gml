graph [
  node [
    id 0
    label 1
    disk 9
    cpu 1
    memory 14
  ]
  node [
    id 1
    label 2
    disk 1
    cpu 3
    memory 3
  ]
  node [
    id 2
    label 3
    disk 9
    cpu 1
    memory 5
  ]
  node [
    id 3
    label 4
    disk 5
    cpu 3
    memory 16
  ]
  node [
    id 4
    label 5
    disk 9
    cpu 3
    memory 15
  ]
  node [
    id 5
    label 6
    disk 10
    cpu 2
    memory 15
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 25
    bw 67
  ]
  edge [
    source 0
    target 1
    delay 25
    bw 167
  ]
  edge [
    source 0
    target 2
    delay 33
    bw 73
  ]
  edge [
    source 1
    target 3
    delay 28
    bw 55
  ]
  edge [
    source 2
    target 5
    delay 31
    bw 190
  ]
  edge [
    source 3
    target 4
    delay 30
    bw 59
  ]
]
