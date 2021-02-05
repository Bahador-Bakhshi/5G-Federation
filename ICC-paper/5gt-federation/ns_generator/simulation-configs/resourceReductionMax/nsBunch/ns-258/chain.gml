graph [
  node [
    id 0
    label 1
    disk 5
    cpu 4
    memory 16
  ]
  node [
    id 1
    label 2
    disk 9
    cpu 3
    memory 16
  ]
  node [
    id 2
    label 3
    disk 2
    cpu 4
    memory 1
  ]
  node [
    id 3
    label 4
    disk 3
    cpu 4
    memory 8
  ]
  node [
    id 4
    label 5
    disk 2
    cpu 2
    memory 3
  ]
  node [
    id 5
    label 6
    disk 10
    cpu 3
    memory 13
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 28
    bw 59
  ]
  edge [
    source 0
    target 1
    delay 34
    bw 104
  ]
  edge [
    source 0
    target 2
    delay 29
    bw 195
  ]
  edge [
    source 0
    target 3
    delay 29
    bw 190
  ]
  edge [
    source 1
    target 4
    delay 25
    bw 185
  ]
  edge [
    source 4
    target 5
    delay 33
    bw 174
  ]
]
