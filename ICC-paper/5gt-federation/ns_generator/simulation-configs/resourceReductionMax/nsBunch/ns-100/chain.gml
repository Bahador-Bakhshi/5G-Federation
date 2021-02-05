graph [
  node [
    id 0
    label 1
    disk 1
    cpu 3
    memory 4
  ]
  node [
    id 1
    label 2
    disk 5
    cpu 1
    memory 3
  ]
  node [
    id 2
    label 3
    disk 5
    cpu 4
    memory 5
  ]
  node [
    id 3
    label 4
    disk 7
    cpu 1
    memory 1
  ]
  node [
    id 4
    label 5
    disk 7
    cpu 2
    memory 14
  ]
  node [
    id 5
    label 6
    disk 8
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
    delay 33
    bw 179
  ]
  edge [
    source 0
    target 1
    delay 30
    bw 197
  ]
  edge [
    source 0
    target 2
    delay 26
    bw 70
  ]
  edge [
    source 0
    target 3
    delay 31
    bw 131
  ]
  edge [
    source 1
    target 4
    delay 35
    bw 132
  ]
  edge [
    source 3
    target 5
    delay 33
    bw 90
  ]
]
